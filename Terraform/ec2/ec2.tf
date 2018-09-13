variable "subnet_id" {}
variable "private_ip" {}
variable "key_name" {}

variable "security_groups" {
  type = "list"
}


resource "aws_instance" "internal_instance" {
  ami           = "ami-51537029"
  instance_type = "t2.micro"
  private_ip = "${var.private_ip}"
  subnet_id = "${var.subnet_id}"
  security_groups = ["${var.security_groups}"]
  key_name = "${var.key_name}"
}