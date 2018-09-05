variable "access_key" {}
variable "secret_key" {}
variable "region" {}

variable "vpc_cidr" {}
variable "name" {}
variable "priv_subnets" {}
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

module "priv_subnet" {
  source = "./priv_subnet"
  name = "${var.name}_inside"
  
  vpc_id = "${module.vpc.vpc_id}"
  subnet_block = "${var.priv_subnets}"
  azns = "${var.azns}"
  
}





#resource "aws_instance" "test" {
#  ami           = "ami-51537029"
#  instance_type = "t2.micro"
#  
#}