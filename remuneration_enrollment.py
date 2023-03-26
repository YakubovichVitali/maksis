from decimal import Decimal

from user.models import MaksisUser


class RemunerationEnrollment:

    def execute(self):
        ref_users = MaksisUser.objects.all()
        ref_users.update(
            replenishment=Decimal('120'),
            remuneration=Decimal('0'),
        )


renumeration_enrollment = RemunerationEnrollment()
