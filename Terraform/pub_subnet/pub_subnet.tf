variable "vpc_id" {}
variable "subnet_block" {}
variable "azns" {}
variable "name" {
  default ="public"
}
variable "propagating_vgws" {
    type = "list"
}

resource "aws_internet_gateway" "public" {
    vpc_id = "${var.vpc_id}"
    tags {
        Name = "${var.name}"
    }
  
}

resource "aws_subnet" "public" {
  vpc_id = "${var.vpc_id}"
  cidr_block = "${var.subnet_block}"
  availability_zone = "${var.azns}"


  tags {
    Name = "internal"
    Subnet_Type = "public"
  }
}

resource "aws_route_table" "public" {
    vpc_id = "${var.vpc_id}"
    propagating_vgws = ["${var.propagating_vgws}"]

}

resource "aws_route" "default_route" {
  route_table_id = "${aws_route_table.public.id}"
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = "${aws_internet_gateway.public.id}"
  depends_on = ["aws_route_table.public"]
}

resource "aws_route_table_association" "public" {
  subnet_id = "${aws_subnet.public.id}"
  route_table_id = "${aws_route_table.public.id}"
}

output "subnet_ids" {
    value = "${aws_subnet.public.id}"
}

output "route_table_ids" {
    value = "${aws_internet_gateway.public.id}"
}