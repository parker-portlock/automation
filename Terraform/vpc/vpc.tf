variable "name" {
  default = "vpc"
}
variable "cidr" {}

resource "aws_vpc" "vpc" {
  cidr_block = "${var.cidr}"
  enable_dns_hostnames = false
  enable_dns_support  = false

  tags{
    Name = "${var.name}"
  }
}

output "vpc_id" {
  value = "${aws_vpc.vpc.id}"
}