import type { SignInRequest, SignInResponse } from '~/types/dtos/sign_in';
import type { SignUpRequest, SignUpResponse } from '~/types/dtos/sign_up';

export default () => {
  const sign_in = async (request: SignInRequest) =>
    $fetch<SignInResponse>(`${api}/user/login`, {
      method: 'POST',
      body: request,
    });

  const sign_up = async (request: SignUpRequest) =>
    $fetch<SignUpResponse>(`${api}/user/register`, {
      method: 'POST',
      body: request,
    });

  return {
    auth: {
      sign_in,
      sign_up,
    },
  };
};
