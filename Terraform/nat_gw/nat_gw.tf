variable "name" {
    default = "nat"
}
variable "azns" {}

variable "public_subnet_ids" {}
resource "aws_eip" "nat" {
    vpc = true


}
resource "aws_nat_gateway" "natgw" {
  
allocation_id = "${aws_eip.nat.id}"
subnet_id = "${var.public_subnet_ids}"

}

output "nat_gateway_ids" {
    value = "${aws_nat_gateway.natgw.id}"
}
