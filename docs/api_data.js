define({ "api": [
  {
    "type": "get",
    "url": "/common/code",
    "title": "Response code description,not actually a api",
    "version": "0.1.0",
    "name": "CommonCode",
    "group": "Common",
    "success": {
      "examples": [
        {
          "title": "Success-Response:",
          "content": "{\n    0: \"Request OK\",\n    40: \"Params error\",\n    41: \"Password error\",\n    42: \"User not exists\",\n    43: \"User exists\",\n    50: \"Internal error\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "apps/util/constant.py",
    "groupTitle": "Common"
  },
  {
    "type": "post",
    "url": "/user/:id/exists",
    "title": "Check whether user exists",
    "version": "0.1.0",
    "name": "UserExists",
    "group": "User",
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>success code.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "404": [
          {
            "group": "404",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/user/handler.py",
    "groupTitle": "User"
  },
  {
    "type": "get",
    "url": "/user/:id",
    "title": "Get user information",
    "version": "0.1.0",
    "name": "UserInfo",
    "group": "User",
    "permission": [
      {
        "name": "Authentication"
      }
    ],
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The access token.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "{\n    \"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The access token.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"nickname\": \"Edgar\",\n    \"email\": \"doforce@126.com\",\n    \"avatar\": null,\n    \"gender\": 0,\n    \"city\": null,\n    \"summary\": null\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "4xx": [
          {
            "group": "4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/user/handler.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/user/:id/login",
    "title": "Login",
    "version": "0.1.0",
    "name": "UserLogin",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>The login password of the user.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "201": [
          {
            "group": "201",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The access token.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 201 Created\n{\n    \"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "4xx": [
          {
            "group": "4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/user/handler.py",
    "groupTitle": "User"
  },
  {
    "type": "post",
    "url": "/user/:id",
    "title": "Registration",
    "version": "0.1.0",
    "name": "UserRegistration",
    "group": "User",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>The password of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>The email of the user.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "201": [
          {
            "group": "201",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>The success code.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "4xx": [
          {
            "group": "4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/user/handler.py",
    "groupTitle": "User"
  },
  {
    "type": "put",
    "url": "/user/:id",
    "title": "Update user information",
    "version": "0.1.0",
    "name": "UserUpdate",
    "group": "User",
    "permission": [
      {
        "name": "Authentication"
      }
    ],
    "header": {
      "fields": {
        "Header": [
          {
            "group": "Header",
            "type": "String",
            "optional": false,
            "field": "token",
            "description": "<p>The access token.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Header-Example:",
          "content": "{\n    \"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6IkVkZ2FyIiwiaWF0IjoxNTQ2MzYxMDQ1LCJleHAiOjE1NDY5NjU4NDV9.zqwf8aemhrH17CZaEt2SKPojpd68OqIcPJfTClAkuC0\"\n}",
          "type": "json"
        }
      ]
    },
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "nickname",
            "description": "<p>The nickname of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "password",
            "description": "<p>The password of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "email",
            "description": "<p>The email of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "avatar",
            "description": "<p>The avatar url of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "gender",
            "description": "<p>The gender of the user, 0 is male, 1 is female.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "String",
            "description": "<p>city The city where user often lives.</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "code",
            "description": "<p>The success code.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "4xx": [
          {
            "group": "4xx",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/user/handler.py",
    "groupTitle": "User"
  }
] });
