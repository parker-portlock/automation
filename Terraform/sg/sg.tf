variable "vpc_id" {}

resource "aws_security_group" "allow_common" {
  name = "allow_common"
  description = "allows common inbound to instances."
  vpc_id = "${var.vpc_id}"

  ingress {
      from_port = 22
      to_port = 22
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
      from_port = 80
      to_port = 80
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
    ingress {
      from_port = 443
      to_port = 443
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
      from_port = 0
      to_port = 0 
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
  }
}

output "sg_id" {
    value = "${aws_security_group.allow_common.id}"
}