class Constant:
    """
    @api {get} /common/code Response code description,not actually a api
    @apiVersion 0.1.0
    @apiName CommonCode
    @apiGroup Common
    @apiSuccessExample {json} Success-Response:
        {
            0:  "Request OK",
            40: "Params error",
            41: "Password error",
            42: "User not exists",
            43: "User exists",
            44: "Resource exists",
            45: "Resource not exists",
            46: "Params insufficiency",
            47: "Unauthorized",
            48: "Bad request",
            50: "Internal error",
        }
    """

    ok = {'code': 0}
    params_error = {'code': 40}
    pwd_error = {'code': 41}
    user_not_exists = {'err': 42}
    user_exists = {'code': 43}
    resource_exists = {'code': 44}
    resource_not_exists = {'code': 45}
    params_insufficiency = {'code': 46}
    unauthorized = {'code': 47}
    bad_request = {'code': 48}
    internal_error = {'code': 50}
