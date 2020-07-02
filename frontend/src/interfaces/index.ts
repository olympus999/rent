export interface IUserProfile {
    id: number;
    email: string;
    first_name: string;
    last_name: string;
    is_active: boolean;
    is_superuser: boolean;
    is_client: boolean;
    is_worker: boolean;
}

export interface IUserProfileUpdate {
    email?: string;
    first_name?: string;
    last_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
    is_client?: boolean;
    is_worker?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    first_name?: string;
    last_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
    is_client?: boolean;
    is_worker?: boolean;
}
