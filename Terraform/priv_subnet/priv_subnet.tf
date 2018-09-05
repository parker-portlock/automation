variable "vpc_id" {}

variable "subnet_block" {}

variable "azns" {}

variable "name" {
  default ="private"
}



resource "aws_subnet" "private" {
  vpc_id = "${var.vpc_id}"
  cidr_block = "${var.subnet_block}"
  availability_zone = "${var.azns}"


  tags {
    Name = "internal"
    Subnet_Type = "private"
  }
}