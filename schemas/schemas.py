from voluptuous import Schema, PREVENT_EXTRA

base_url = "https://reqres.in/"

single_user = Schema(
    {
        "data":
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
        "support":
            {
                "url": str,
                "text": str
            }
    },
    extra=PREVENT_EXTRA,
    required=True

)

create_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

register_user = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

login_user = Schema(
    {
        "token": str,
    },
    extra=PREVENT_EXTRA,
    required=True
)
