variable "vpc_id" {}
variable "subnet_block" {}
variable "azns" {}
variable "name" {
  default ="private"
}
variable "propagating_vgws" {
  type = "list"
}
variable "nat_gateway_ids" {}



resource "aws_subnet" "private" {
  vpc_id = "${var.vpc_id}"
  cidr_block = "${var.subnet_block}"
  availability_zone = "${var.azns}"


  tags {
    Name = "${var.name}_private"
    Subnet_Type = "private"
  }
}

resource "aws_route_table" "private" {
    vpc_id = "${var.vpc_id}"
    propagating_vgws = ["${var.propagating_vgws}"]

}

resource "aws_route" "default_route" {
  route_table_id = "${aws_route_table.private.id}"
  destination_cidr_block = "0.0.0.0/0"
  nat_gateway_id = "${var.nat_gateway_ids}"
  depends_on = ["aws_route_table.private"]
}

resource "aws_route_table_association" "private" {
  subnet_id = "${aws_subnet.private.id}"
  route_table_id = "${aws_route_table.private.id}"
}

output "subnet_ids" {
    value = "${aws_subnet.private.id}"
}