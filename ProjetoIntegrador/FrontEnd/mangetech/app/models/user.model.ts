export class User {
    id: number = 0;
    name: string = "";
    email: string = "";
    nif: string = "";
    phone: string = "";
    is_staff: boolean = false;
    is_active: boolean = false;
    creation_date: Date = new Date();
    photo: string = "";
}