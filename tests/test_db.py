from sqlalchemy import select

from fastzero.models import User


def test_create_user(session):
    user = User(
        username='Ana Quézia',
        password='quezia2006',
        email='anaquezia200106@gmail.com',
    )

    session.add(user)
    session.commit()
    session.refresh(user)
    result = session.scalar(
        select(User).where(User.email == 'freireyago51@gmail.com')
    )

    # assert result.username == 'Yago Freire'
    # assert result.id == 1
