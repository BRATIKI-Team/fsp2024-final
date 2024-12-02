export interface SignInRequest {
  readonly email: string;
  readonly password: string;
}

export interface SignInResponse {
  readonly id: string;
  readonly email: string;
  readonly token: string;
  readonly refresh_token: string;
}
