##################################################################################
# region - The VPC region to create the TMOS VPC Custom Image
##################################################################################
variable "region" {
  type        = string
  default     = "us-south"
  description = "The VPC region to create the TMOS VPC Custom Image"
}

# Present for CLI testng
#variable "api_key" {
#  type        = string
#  default     = ""
#  description = "IBM Public Cloud API KEY"
#}
