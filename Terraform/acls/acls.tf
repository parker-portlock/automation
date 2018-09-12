variable "vpc_id" {}
variable "subnet_block" {}
variable "name" {}

resource "aws_network_acl" "test_acl" {
    vpc_id = "${var.vpc_id}"
    
    egress {
        protocol = "all"
        rule_no = 10
        action = "allow"
        cidr_block = "${var.subnet_block}"
        from_port = 0
        to_port = 0
    }

    ingress {
        protocol = "all"
        rule_no = 20
        action = "allow"
        cidr_block = "${var.subnet_block}"
        from_port = 0
        to_port = 0
    }

    tags {
        Name = "internal"
    }
}
