# get the public image COS SQL url and default name
data "external" "schematics_env" {
  program = ["python", "${path.module}/source_env.py"]
}

output "schematics_env" {
  value = data.external.schematics_env.result
}
