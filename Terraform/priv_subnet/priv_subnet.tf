variable "vpc_id" {}

variable "subnet_block" {}

variable "region" {
  
}
variable "name" {
  default ="private"
}



resource "aws_subnet" "private" {
  vpc_id = "${var.vpc_id}"
  cidr_block = "${var.subnet_block}"
  availability_zone = "${var.region}"


  tags {
    Name = "internal"
    Subnet_Type = "private"
  }
}