import type { PageServerLoad } from './$types';
import { error, redirect, fail } from '@sveltejs/kit';
import PocketBase from 'pocketbase';

export const load = (async ({ locals }) => {
	if (locals.pb.authStore.isValid) {
		throw redirect(303, '/');
	}
	return {
		user: locals.user
	};
}) satisfies PageServerLoad;

export const actions = {
	login: async ({ request, locals }) => {
		const pb = new PocketBase('https://pocketbase-test.tysonjenkins.dev');
		const formData = await request.formData();
		const username = formData.get('username') as string;
		const password = formData.get('password') as string;

		try {
			await locals.pb
				.collection('users')
				.authWithPassword(username.toString(), password.toString());
		} catch (err: any) {
			console.log(err);
      return fail(400, {
        error: "Username or Password is incorrect"
      })
		}
		throw redirect(303, '/');
	}
};
