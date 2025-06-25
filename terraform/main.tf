provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "my_bucket" {
  bucket = "srikanth-tf-bucket-2027"

  tags = {
    Name        = "DE Prac Bucket"
    Environment = "Dev"
  }
}
