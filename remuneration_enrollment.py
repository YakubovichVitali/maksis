from decimal import Decimal
from typing import Optional

from django.db.models import F

from user.models import MaksisUser


class RemunerationEnrollment:

    LEVEL_1 = 1
    LEVEL_2 = 2
    LEVEL_3 = 3
    LEVEL_4 = 4
    LEVEL_5 = 5
    LEVEL_6 = 6

    MAPPING_MONEY = {
        LEVEL_1: Decimal('30'),
        LEVEL_2: Decimal('40'),
        LEVEL_3: Decimal('50'),
        LEVEL_4: Decimal('60'),
        LEVEL_5: Decimal('65'),
        LEVEL_6: Decimal('70'),
    }

    MAPPING_LEVEL = {
        LEVEL_2: {
            LEVEL_1: Decimal('10'),
        },
        LEVEL_3: {
            LEVEL_1: Decimal('20'),
            LEVEL_2: Decimal('10'),
        },
        LEVEL_4: {
            LEVEL_1: Decimal('30'),
            LEVEL_2: Decimal('20'),
            LEVEL_3: Decimal('10'),
        },
        LEVEL_5: {
            LEVEL_1: Decimal('35'),
            LEVEL_2: Decimal('25'),
            LEVEL_3: Decimal('15'),
            LEVEL_4: Decimal('5'),
        },
        LEVEL_6: {
            LEVEL_1: Decimal('40'),
            LEVEL_2: Decimal('30'),
            LEVEL_3: Decimal('20'),
            LEVEL_4: Decimal('10'),
            LEVEL_5: Decimal('5'),
        },
    }

    def execute(self):
        ref_users = MaksisUser.objects.all()
        ref_users.update(
            replenishment=Decimal('120'),
            remuneration=Decimal('0'),
        )

        ref_users = ref_users.filter(
            children__isnull=False,
        ).distinct()

        for ref_user in ref_users.iterator():
            self._update_remuneration(
                ref_user=ref_user,
                ref_level=ref_user.ref_level,
            )

    def _update_remuneration(
            self,
            ref_user: MaksisUser,
            ref_level: int,
            remuneration: Optional[Decimal] = None,
            count_invited_users: Optional[int] = None,
    ) -> None:
        remuneration = remuneration or self.MAPPING_MONEY[ref_user.ref_level]
        count = count_invited_users or ref_user.children.count()

        ref_user.remuneration = F('remuneration') + count * remuneration
        ref_user.save(update_fields=('remuneration',))

        if ref_user.ref_level != self.LEVEL_1:
            self._update_remuneration(
                ref_user=ref_user.parent,
                ref_level=ref_level,
                remuneration=self.MAPPING_LEVEL[ref_level][ref_user.parent.ref_level],
                count_invited_users=count,
            )


remuneration_enrollment = RemunerationEnrollment()
