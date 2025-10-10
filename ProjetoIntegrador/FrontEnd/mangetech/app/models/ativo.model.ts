import { Ambiente } from "./ambiente.model";

export class Ativo {
    id: number = 0;
    name: string = "";
    code: string = "";
    description: string = "";
    creation_date: Date = new Date();
    category_FK: string = "";
    environment_FK: Ambiente = new Ambiente();
}