import { IUserProfile, IUserRole } from '@/interfaces';

export interface AdminState {
    users: IUserProfile[];
    usersRoles: IUserRole[];
}
