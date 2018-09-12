variable "access_key" {}
variable "secret_key" {}
variable "region" {}
variable "vpc_cidr" {}
variable "name" {}
variable "priv_subnets" {}
variable "pub_subnets" {}
variable "enc_domain" {}
variable "vpn_peer" {}

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


module "acls" {
  source = "./acls"
  name = "${var.name}_acl"
  
  vpc_id = "${module.vpc.vpc_id}"
  subnet_block = "${var.priv_subnets}"
  
  }



#resource "aws_instance" "test" {
#  ami           = "ami-51537029"
#  instance_type = "t2.micro"
#  
#}