export interface IUserTool {
  id: number;
  user_id: number;
  tool_id: number;
  details?: string;
}

export interface IUserToolCreate {
  user_id: number;
  tool_id: number;
  details?: string;
}

export interface IUserToolUpdate {
  id: number;
  tool_id: number;
  details?: string;
}