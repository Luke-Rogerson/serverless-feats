resource "aws_cognito_user_pool" "pool" {
  name                = "feats-cognito"
  username_attributes = ["email"]

  schema {
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = true
    name                     = "email"
    required                 = true

    string_attribute_constraints {
      min_length = 7
      max_length = 256
    }
  }

  schema {
    attribute_data_type      = "String"
    developer_only_attribute = false
    mutable                  = true
    name                     = "name"
    required                 = true

    number_attribute_constraints {
      min_value = 1
      max_value = 256
    }
  }


  admin_create_user_config {
    allow_admin_create_user_only = true
  }

  account_recovery_setting {
    recovery_mechanism {
      name     = "verified_email"
      priority = 1
    }
  }

  password_policy {
    minimum_length = 12
  }

}

resource "aws_cognito_user_pool_client" "client" {
  name                 = "client"
  user_pool_id         = aws_cognito_user_pool.pool.id
  allowed_oauth_flows  = ["code", "implicit"]
  allowed_oauth_scopes = ["openid", "email"]
  callback_urls        = ["https://${var.cognito_domain}/callback"]
  logout_urls          = ["https://${var.cognito_domain}/signout"]
}

resource "aws_cognito_user_pool_domain" "serverlessfeats" {
  domain       = var.cognito_domain
  user_pool_id = aws_cognito_user_pool.pool.id
}

