class Constant:
    """
    @api {get} /common/code Response code description,not actually a api
    @apiVersion 0.1.0
    @apiName CommonCode
    @apiGroup Common
    @apiSuccessExample {json} Success-Response:
        {
            0: "Request OK",
            40: "Params error",
            41: "Password error",
            42: "User not exists",
            43: "User exists",
            50: "Internal error",
        }
    """

    ok = {'code': 0}
    params_error = {'code': 40}
    pwd_error = {'code': 41}
    user_not_exists = {'err': 42}
    user_exists = {'code': 43}
    internal_error = {'code': 50}

