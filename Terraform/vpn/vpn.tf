variable "peerip" {}
variable "name" {}
variable "vpg_id" {}
variable "dest_enc_domain" {}

resource "aws_customer_gateway" "cgw" {
  bgp_asn = 65000
  ip_address = "${var.peerip}"
  type = "ipsec.1"

  tags {
      Name = "${var.name}_vpn"
  }
}

resource "aws_vpn_connection" "vpn" {
  vpn_gateway_id = "${var.vpg_id}"
  customer_gateway_id = "${aws_customer_gateway.cgw.id}"
  type = "ipsec.1"
  static_routes_only = true
  
  tags {
    Name = "Test_VPN"
  }
}

resource "aws_vpn_connection_route" "home" {
  destination_cidr_block = "${var.dest_enc_domain}"
  vpn_connection_id = "${aws_vpn_connection.vpn.id}"
}

output "cgw_id" {
  value = "${aws_customer_gateway.cgw.id}"
}
output "vpn1_psk" {
  value = "${aws_vpn_connection.vpn.tunnel1_preshared_key}"
}
output "vpn1_addr" {
  value = "${aws_vpn_connection.vpn.tunnel1_address}"
}
output "vpn2_psk" {
    value = "${aws_vpn_connection.vpn.tunnel2_preshared_key}"
}
output "vpn2_addr" {
  value = "${aws_vpn_connection.vpn.tunnel2_address}"
}

