from crud import create_user
from fastapi import APIRouter, Body, status
from fastapi.responses import JSONResponse
from scheme import UserCreate, UserOut
from utils import make_message

router = APIRouter()


@router.get("/get")
def get_test():
    return {"message": "test"}


@router.post("/create", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def create(
    user: UserCreate = Body(
        example={
            "nick_name": "test",
            "password": "1234",
            "email": "test@email.com",
        }
    )
):
    try:
        new_user = create_user(user)
        # https://stackoverflow.com/questions/71467630/fastapi-issues-with-mongodb-typeerror-objectid-object-is-not-iterable?noredirect=1&lq=1
        new_user.pop("_id")
        # TODO
        # _id 처리 방법 생각하기
    except Exception:
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content=make_message("서버 에러"),
        )
    return new_user


# TODO
# dummy dataset read
# dummy dataset 만드는 api 작성
# dummy dataset 전부 삭제
# dummy dataset 지정 삭제