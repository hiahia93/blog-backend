define({ "api": [
  {
    "type": "post",
    "url": "/article",
    "title": "Create an article",
    "version": "0.1.0",
    "name": "ArticleCreate",
    "group": "Article",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "string",
            "optional": false,
            "field": "title",
            "description": "<p>The title of the article</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": false,
            "field": "content",
            "description": "<p>The content of the article</p>"
          },
          {
            "group": "Parameter",
            "type": "Number[]",
            "optional": true,
            "field": "labels",
            "description": "<p>The label ids that will be binding the article</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "201": [
          {
            "group": "201",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The created article id.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "400": [
          {
            "group": "400",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/article/handler.py",
    "groupTitle": "Article"
  },
  {
    "type": "delete",
    "url": "/article/:id",
    "title": "Delete an article",
    "version": "0.1.0",
    "name": "ArticleDelete",
    "group": "Article",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The successful code.</p>"
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
    "filename": "apps/article/handler.py",
    "groupTitle": "Article"
  },
  {
    "type": "post",
    "url": "/article/:article_id/label/:label_id",
    "title": "Tag an article",
    "version": "0.1.0",
    "name": "ArticleTag",
    "group": "Article",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The created article id.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "400": [
          {
            "group": "400",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/article/handler.py",
    "groupTitle": "Article"
  },
  {
    "type": "delete",
    "url": "/article/:article_id/label/:label_id",
    "title": "Delete a label for an article",
    "version": "0.1.0",
    "name": "ArticleUnTag",
    "group": "Article",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The created article id.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "400": [
          {
            "group": "400",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/article/handler.py",
    "groupTitle": "Article"
  },
  {
    "type": "put",
    "url": "/article/:id",
    "title": "Update an article",
    "version": "0.1.0",
    "name": "ArticleUpdate",
    "group": "Article",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "string",
            "optional": true,
            "field": "title",
            "description": "<p>The new title of the article</p>"
          },
          {
            "group": "Parameter",
            "type": "string",
            "optional": true,
            "field": "content",
            "description": "<p>The new content of the article</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The successful code.</p>"
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
    "filename": "apps/article/handler.py",
    "groupTitle": "Article"
  },
  {
    "type": "get",
    "url": "/article?article_id=0&start=0&limit=10&label_id=1",
    "title": "Get some articles, a specific article default",
    "version": "0.1.0",
    "name": "Articles",
    "group": "Article",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "article_id",
            "description": "<p>The id of this article, return this article's information</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "start",
            "defaultValue": "0",
            "description": "<p>The begin page number of the articles</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>The count of the articles that will be returned</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "label_id",
            "description": "<p>The label id that articles catch</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object[]",
            "optional": false,
            "field": "items",
            "description": "<p>the articles object array</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n   \"items\": [\n       \"id\": 1,\n       \"title\": \"Hello\",\n       \"content\": \"I am Edgar, welcome to my world.\",\n       \"views\": 2333,\n       \"created_at\": 1546414975,\n       \"updated_at\": 1546414975,\n   ]\n}",
          "type": "json"
        }
      ]
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
    "filename": "apps/article/handler.py",
    "groupTitle": "Article"
  },
  {
    "type": "post",
    "url": "/auth",
    "title": "Get access token",
    "version": "0.1.0",
    "name": "AuthAccessToken",
    "group": "Auth",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "id",
            "description": "<p>JSON param, the id of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>JSON param, the login password of the user.</p>"
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
    "filename": "apps/handlers.py",
    "groupTitle": "Auth"
  },
  {
    "type": "get",
    "url": "/comment?comment_id=0&label_id=0&start=0&limit=10",
    "title": "Get some comments of a article, a specific comment default",
    "version": "0.1.0",
    "name": "ArticleComments",
    "group": "Comment",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "comment_id",
            "description": "<p>The id of a specific comment</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "start",
            "defaultValue": "0",
            "description": "<p>The begin page number of the comments</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "limit",
            "defaultValue": "10",
            "description": "<p>The count of the comments that will be returned</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "article_id",
            "description": "<p>The article id that the comments were on</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object[]",
            "optional": false,
            "field": "items",
            "description": "<p>the articles object array</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"items\": [\n        \"id\": 1,\n        \"title\": \"Hello\",\n        \"content\": \"I am Edgar, welcome to my world.\",\n        \"views\": 2333,\n        \"created_at\": 1546414975,\n        \"updated_at\": 1546414975,\n    ]\n}",
          "type": "json"
        }
      ]
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
    "filename": "apps/comment/handler.py",
    "groupTitle": "Comment"
  },
  {
    "type": "post",
    "url": "/comment",
    "title": "Get some comments of a article",
    "version": "0.1.0",
    "name": "CommentCreate",
    "group": "Comment",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "article_id",
            "description": "<p>JSON param, the id of a article</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "content",
            "description": "<p>JSON param, a comment content</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "201": [
          {
            "group": "201",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The successful code</p>"
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
            "description": "<p>The error code</p>"
          }
        ]
      }
    },
    "filename": "apps/comment/handler.py",
    "groupTitle": "Comment"
  },
  {
    "type": "delete",
    "url": "/comment/:id",
    "title": "Delete a comment",
    "version": "0.1.0",
    "name": "CommentDelete",
    "group": "Comment",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The successful code.</p>"
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
    "filename": "apps/comment/handler.py",
    "groupTitle": "Comment"
  },
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
          "content": "{\n    0:  \"Request OK\",\n    40: \"Params error\",\n    41: \"Password error\",\n    42: \"User not exists\",\n    43: \"User exists\",\n    44: \"Resource exists\",\n    45: \"Resource not exists\",\n    46: \"Params insufficiency\",\n    47: \"Unauthorized\",\n    48: \"Bad request\",\n    50: \"Internal error\",\n}",
          "type": "json"
        }
      ]
    },
    "filename": "apps/util/constant.py",
    "groupTitle": "Common"
  },
  {
    "type": "post",
    "url": "/label",
    "title": "Create a label",
    "version": "0.1.0",
    "name": "UserCreate",
    "group": "Label",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "string",
            "optional": false,
            "field": "label",
            "description": "<p>JSON param, the label name</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "201": [
          {
            "group": "201",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>The created label id.</p>"
          }
        ]
      }
    },
    "error": {
      "fields": {
        "400": [
          {
            "group": "400",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The error code.</p>"
          }
        ]
      }
    },
    "filename": "apps/label/handler.py",
    "groupTitle": "Label"
  },
  {
    "type": "delete",
    "url": "/label/:id",
    "title": "Delete a label",
    "version": "0.1.0",
    "name": "UserDelete",
    "group": "Label",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The successful code.</p>"
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
    "filename": "apps/label/handler.py",
    "groupTitle": "Label"
  },
  {
    "type": "get",
    "url": "/label",
    "title": "Get some labels, all labels in server default if article_id is not given",
    "version": "0.1.0",
    "name": "UserGetAll",
    "group": "Label",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "article_id",
            "description": "<p>JSON param, the id of this article, return this article's labels</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Object[]",
            "optional": false,
            "field": "items",
            "description": "<p>The label name and its id array.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"items\": [\n        {\n        \"id\": 1,\n        \"label\": \"Android\"\n        },\n        {\n        \"id\": 2,\n        \"label\": \"Java\"\n        }\n    ]\n}",
          "type": "json"
        }
      ]
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
    "filename": "apps/label/handler.py",
    "groupTitle": "Label"
  },
  {
    "type": "put",
    "url": "/label/:id",
    "title": "Update a label",
    "version": "0.1.0",
    "name": "UserUpdate",
    "group": "Label",
    "permission": [
      {
        "name": "Authorized"
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
            "type": "string",
            "optional": false,
            "field": "label",
            "description": "<p>JSON param, the new label name</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "200": [
          {
            "group": "200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>The successful code.</p>"
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
    "filename": "apps/label/handler.py",
    "groupTitle": "Label"
  },
  {
    "type": "get",
    "url": "/user?check=y&id=john",
    "title": "Get user information",
    "version": "0.1.0",
    "name": "UserInfo",
    "group": "User",
    "permission": [
      {
        "name": "Authorized"
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
            "field": "check",
            "description": "<p>just check if the user exists</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "id",
            "description": "<p>A Unauthorized user id, only use when a check param was given</p>"
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
            "field": "nickname",
            "description": "<p>The nickname of the user.</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>The email of the user.</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "avatar",
            "description": "<p>The avatar url of the user.</p>"
          },
          {
            "group": "200",
            "type": "Number",
            "optional": false,
            "field": "gender",
            "description": "<p>The gender of the user, 0 is male, 1 is female.</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "city",
            "description": "<p>The city where user often lives.</p>"
          },
          {
            "group": "200",
            "type": "String",
            "optional": false,
            "field": "summary",
            "description": "<p>The brief introduction of the user.</p>"
          },
          {
            "group": "200",
            "type": "Number",
            "optional": true,
            "field": "code",
            "description": "<p>Only return when you given a specific check param.</p>"
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
            "field": "id",
            "description": "<p>JSON param, the id of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "password",
            "description": "<p>JSON param, the password of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "email",
            "description": "<p>JSON param, the email of the user.</p>"
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
            "description": "<p>The successful code.</p>"
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
    "url": "/user",
    "title": "Update user information",
    "version": "0.1.0",
    "name": "UserUpdate",
    "group": "User",
    "permission": [
      {
        "name": "Authorized"
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
            "description": "<p>JSON param, the nickname of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "password",
            "description": "<p>JSON param, the password of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "avatar",
            "description": "<p>JSON param, the avatar url of the user.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": true,
            "field": "gender",
            "description": "<p>JSON param, the gender of the user, 0 is male, 1 is female.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "city",
            "description": "<p>JSON param, the city where user often lives.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": true,
            "field": "summary",
            "description": "<p>JSON param, the brief introduction of the user.</p>"
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
            "description": "<p>The successful code.</p>"
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
