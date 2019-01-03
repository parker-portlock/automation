
variable "region" {}
variable "vpc_cidr" {}
variable "name" {}
variable "priv_subnets" {}
variable "pub_subnets" {}
variable "enc_domain" {}
variable "vpn_peer" {}
variable "inst_ip" {}
variable "azns" {
    default ="us-west-2a"
}

#Provider Definition#
provider "aws" {
#  shared_credentials_file = "/Users/parker.portlock/.aws/credentials"
  region = "${var.region}"
}

#VPC Creation#
module "vpc" {
  source = "./vpc"
  
  name = "${var.name}_vpc"
  cidr = "${var.vpc_cidr}"
}

#Creates public subnet#
module "pub_subnet" {
  source = "./pub_subnet"
  name = "${var.name}_dmz"
  
  vpc_id = "${module.vpc.vpc_id}"
  subnet_block = "${var.pub_subnets}"
  azns = "${var.azns}"
  propagating_vgws = ["${module.vpg.vpg_id}"]
  
}

#Creates NAT Gateway#
module "nat_gw" {
  source = "./nat_gw"

  name = "${var.name}_nat"
  azns = "${var.azns}"
  public_subnet_ids = "${module.pub_subnet.subnet_ids}"

}

#Creates Private Subnet#
module "priv_subnet" {
  source = "./priv_subnet"
  name = "${var.name}_inside"
  
  vpc_id = "${module.vpc.vpc_id}"
  subnet_block = "${var.priv_subnets}"
  azns = "${var.azns}"
  propagating_vgws = ["${module.vpg.vpg_id}"]
  nat_gateway_ids = "${module.nat_gw.nat_gateway_ids}"
  
}

#Creates Virtual Private Gateway#
module "vpg" {
  source = "./vpg"
  name = "${var.name}_vpg"
  vpc_id = "${module.vpc.vpc_id}"
  
}

#Creates VPN Connection#
module "vpn" {
  source = "./vpn"
  name = "${var.name}_vpn"
  vpg_id = "${module.vpg.vpg_id}"
  dest_enc_domain = "${var.enc_domain}"
  peerip ="${var.vpn_peer}"
}


#Creates Service Group#
module "sg" {
    source = "./sg"
    vpc_id = "${module.vpc.vpc_id}"
}

#Creates Key Pair for Instance#
#resource "aws_key_pair" "pportlock" {
#  key_name = "pportlock"
#  public_key = "${var.public_key}"
#
#}


#Creates Test Instance#
module "ec2" {
  source = "./ec2"
  private_ip = "${var.inst_ip}"
  subnet_id = "${module.priv_subnet.subnet_ids}"
  security_groups = ["${module.sg.sg_id}"]
  key_name = "pportlock"
}


output "vpn1_address" {
  value = "${module.vpn.vpn1_addr}"
}
output "vpn1_psk" {
  value = "${module.vpn.vpn1_psk}"
}
output "vpn2_address" {
  value = "${module.vpn.vpn2_addr}"
}
output "vpn2_psk" {
  value = "${module.vpn.vpn2_psk}"
}