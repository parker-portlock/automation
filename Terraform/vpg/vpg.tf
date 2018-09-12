variable "name" {
    default = "vpg"
}

variable "vpc_id" {}

resource "aws_vpn_gateway" "vpn_gw" {
  vpc_id = "${var.vpc_id}"

  tags  {
      Name = "${var.name}"
  }
}

output "vpg_id" {
    value = "${aws_vpn_gateway.vpn_gw.id}"
}