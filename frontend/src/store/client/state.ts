import {IWorkerProfile, IProject} from '@/interfaces';

export interface ClientState {
  workers: IWorkerProfile[];
  projects: IProject[]
}
