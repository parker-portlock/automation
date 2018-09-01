
variable "access_key" {}
variable "secret_key" {}
variable "region"{
  default ="us-west-2"
}

provider "aws" {
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
  region = "${var.region}"
}

variable "cidr_block"{}
variable "vpc_id" {
  
}


resource "aws_vpc" "vpc_test"{
  id ="${var.vpc_id}"
  cidr_block = "${var.cidr_block}"
  default = true

}

variable "subnet_id"{}
variable "subnet_block"{}
resource "aws_subnet" "internal" {
  vpc_id = "${var.vpc_id}"
  cidr_block = "${var.subnet_block}"
  id = "${var.subnet_id}"

}








#resource "aws_instance" "test" {
#  ami           = "ami-51537029"
#  instance_type = "t2.micro"
#  
#}