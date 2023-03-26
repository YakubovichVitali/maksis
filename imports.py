import json
from typing import (
    List,
    Optional,
)

from user.models import MaksisUser


class ImportReferralUsers:

    def execute(self) -> None:
        with open('data.json') as file_data:
            data = json.load(file_data)

        self._delete_ref_users()

        print('Start creating referral users ...')

        ref_user = self._create_ref_user(
            ref_id=data['id'],
        )

        self._execute(
            parent_id=ref_user.pk,
            refs=data['refs'],
        )

        print('Referral user creation complete')

    def _execute(
            self,
            parent_id: int,
            refs: List[dict],
            ref_level: int = 2,
    ) -> None:
        for ref in refs:
            ref_user = self._create_ref_user(
                ref_id=ref['id'],
                ref_level=ref_level,
                parent_id=parent_id,
            )
            self._execute(
                parent_id=ref_user.pk,
                ref_level=ref_level + 1,
                refs=ref['refs'],
            )

    def _create_ref_user(
            self,
            ref_id: str,
            ref_level: int = 1,
            parent_id: Optional[int] = None,
    ) -> MaksisUser:
        return MaksisUser.objects.create(
            ref_id=ref_id,
            ref_level=ref_level,
            parent_id=parent_id,
        )

    def _delete_ref_users(self) -> None:
        ref_users = MaksisUser.objects.all()
        ref_users.delete()


import_referral_users = ImportReferralUsers()
