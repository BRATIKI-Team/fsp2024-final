export interface SignUpRequest {
  readonly email: string;
  readonly password: string;
}

export type SignUpResponse = boolean;
