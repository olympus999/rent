export interface ITool {
  id: number;
  name: string;
  description?: string;
}

export interface IToolCreate {
  name: string;
  description?: string;
}

export interface IToolUpdate {
  id: number;
  name: string;
  description?: string;
}