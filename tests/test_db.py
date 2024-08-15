from sqlalchemy import select

from fastzero.models import User


def test_create_user(session):
    user = User(
        username='Yago Freire',
        email='freireyago51@gmail.com',
        password='yago123',
    )
    session.add(user)
    session.commit()
    result = session.scalar(
        select(User).where(User.email == 'freireyago51@gmail.com')
    )

    assert result.username == 'Yago Freire'
    assert result.id == 1
