variable "access_key" {}
variable "secret_key" {}
variable "region" {}
variable "vpc_cidr" {}
variable "name" {}
variable "priv_subnets" {}
variable "pub_subnets" {}
variable "enc_domain" {}
variable "vpn_peer" {}
variable "inst_ip" {}
variable "public_key" {}




variable "azns" {
    default ="us-west-2a"
}


provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region = "${var.region}"
}

module "vpc" {
  source = "./vpc"
  
  name = "${var.name}_vpc"
  cidr = "${var.vpc_cidr}"
}
module "pub_subnet" {
  source = "./pub_subnet"
  name = "${var.name}_dmz"
  
  vpc_id = "${module.vpc.vpc_id}"
  subnet_block = "${var.pub_subnets}"
  azns = "${var.azns}"
  propagating_vgws = ["${module.vpg.vpg_id}"]
  
}
module "nat_gw" {
  source = "./nat_gw"

  name = "${var.name}_nat"
  azns = "${var.azns}"
  public_subnet_ids = "${module.pub_subnet.subnet_ids}"

}

module "priv_subnet" {
  source = "./priv_subnet"
  name = "${var.name}_inside"
  
  vpc_id = "${module.vpc.vpc_id}"
  subnet_block = "${var.priv_subnets}"
  azns = "${var.azns}"
  propagating_vgws = ["${module.vpg.vpg_id}"]
  nat_gateway_ids = "${module.nat_gw.nat_gateway_ids}"
  
}

module "vpg" {
  source = "./vpg"
  name = "${var.name}_vpg"
  vpc_id = "${module.vpc.vpc_id}"
  
}

module "vpn" {
  source = "./vpn"
  name = "${var.name}_vpn"
  vpg_id = "${module.vpg.vpg_id}"
  dest_enc_domain = "${var.enc_domain}"
  peerip ="${var.vpn_peer}"
}


resource "aws_network_acl" "public" {
    vpc_id = "${module.vpc.vpc_id}"
    subnet_ids = ["${var.pub_subnets}"]

    egress {
        protocol = "all"
        rule_no = 10
        action = "allow"
        cidr_block = "0.0.0.0/0"
        from_port = 0
        to_port = 0
    }

    ingress {
        protocol = "all"
        rule_no = 10
        action = "deny"
        cidr_block = "0.0.0.0/0"
        from_port = 0
        to_port = 0
    }

    tags {
        Name = "${var.name}_dmz"
    }
}

resource "aws_network_acl" "private" {
    vpc_id = "${module.vpc.vpc_id}"
    subnet_ids = ["${var.priv_subnets}"]

    egress {
        protocol = "all"
        rule_no = 10
        action = "allow"
        cidr_block = "0.0.0.0/0"
        from_port = 0
        to_port = 0
    }

    ingress {
        protocol = "all"
        rule_no = 10
        action = "allow"
        cidr_block = "0.0.0.0/0"
        from_port = 0
        to_port = 0
    }

    tags {
        Name = "${var.name}_internal"
    }
}

module "sg" {
    source = "./sg"
    vpc_id = "${module.vpc.vpc_id}"
}

resource "aws_key_pair" "abm" {
  key_name = "mykey"
  public_key = "${var.public_key}"

}


module "ec2" {
  source = "./ec2"
  private_ip = "${var.inst_ip}"
  subnet_id = "${module.priv_subnet.subnet_ids}"
  security_groups = ["${module.sg.sg_id}"]
  key_name = "${aws_key_pair.abm.key_name}"
}
