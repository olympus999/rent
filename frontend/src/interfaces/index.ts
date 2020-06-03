export interface IUserProfile {
    email: string;
    is_active: boolean;
    is_superuser: boolean;
    first_name: string;
    last_name: string;
    id: number;
}

export interface IUserProfileUpdate {
    email?: string;
    first_name?: string;
    last_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}

export interface IUserProfileCreate {
    email: string;
    first_name?: string;
    last_name?: string;
    password?: string;
    is_active?: boolean;
    is_superuser?: boolean;
}
