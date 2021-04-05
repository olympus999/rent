from typing import Optional
from app import crud, models, schemas
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi import HTTPException
import numpy as np
import datetime

from app.models.project_worker import ProjectWorker
from app.models.project_worker_active import ProjectWorkerActive
from app.models.user import User


def id_to_list(_id):
    return _id if type(_id) is list else [_id]


def update_or_create_project(db: Session,
                             project_in: schemas.ProjectAdminCreateUpdate):
    """
        Specify project_id if updating, otherwise new project will be created.
        @param db: Session
        @param project_in:
    """

    # json_project_in = jsonable_encoder(project_in, exclude_unset=True)
    # json_project_worker_in = jsonable_encoder(project_in.project_worker, exclude_unset=True)
    # print('json_project_in')
    # print(json_project_in)
    # print('json_project_worker_in')
    # print(json_project_worker_in)

    if project_in.id:
        project = crud.project.get_project_with_workers(db, project_in.id)
        # db_obj = crud.project.get(db, project_in.id)
        # crud.project.update(db, db_obj=db_obj, obj_in=project_in)
    else:
        project = crud.project.create(db, obj_in=project_in)
        # project = crud.project.get_project_with_workers(db, created_project.id)

    # json_project_worker = jsonable_encoder(project.project_worker, exclude_unset=True)
    # print('json_project_worker')
    # print(json_project_worker)

    # Update project related fields
    for field in ['name', 'address', 'description']:
        project_in_att = getattr(project_in, field)
        setattr(project, field, project_in_att)

    ppw = project.project_worker
    ppw_in = project_in.project_worker.copy()

    # Update project.project_worker
    # TODO possible bug opportunity. If two different admins have the same window open,
    # TODO then one can remove while other accepts, then the last action will override.
    # Fields to check for changes
    fields = ['removed_dt', 'worker_accepted_dt']
    if len(ppw) > 0:

        # Separate existing project_workers and added ones
        ids_existing = [x.id for x in ppw]
        ids_in = [x.id for x in ppw_in]

        updated_idx = []

        for idx, id_exists in enumerate(ids_existing):
            idx_in = ids_in.index(id_exists)
            updated_idx.append(idx_in)
            pw = ppw[idx]
            pw_in = ppw_in[idx_in]
            for field in fields:
                assert pw.id == pw_in.id
                pw_att = getattr(pw, field)
                pw_in_att = getattr(pw_in, field)
                # If there has been a change apply the change
                if pw_att != pw_in_att and (pw_att is None or pw_in_att is None):
                    # Set new field
                    setattr(pw, field, pw_in_att)
                    # Manage ProjectWorkerActive
                    if field == 'worker_accepted_dt' and pw_in_att is not None:
                        pw.project_worker_active.append(ProjectWorkerActive(user_id=pw_in.worker.id))
                    if field == 'removed_dt' and pw_att is None:
                        pw.project_worker_active = []

        # Remove updated objects, so that only to be added objects remain
        for idx in sorted(updated_idx, reverse=True):
            del ppw_in[idx]

    # Add project.project_worker
    for item in ppw_in:
        pw = ProjectWorker(
            user_id=item.worker.id,
            project_id=21
        )
        for field in fields:
            item_att = getattr(item, field)
            if item_att:
                setattr(pw, field, item_att)
            if field == 'worker_accepted_dt' and item_att is not None:
                pw.project_worker_active.append(ProjectWorkerActive(user_id=item.worker.id))
        ppw.append(pw)

    db.commit()
    db.refresh(project)
    return project
