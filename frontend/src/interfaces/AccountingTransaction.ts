
export interface IAccountingTransaction {
  id: number;
  user_id: number;
  type_id: number;
  amount: string;
  comment?: string;
  created_dt: Date;
}

export interface IAccountingTransactionCreate {
  user_id: number;
  type_id: number;
  amount: string;
  comment?: string;
}