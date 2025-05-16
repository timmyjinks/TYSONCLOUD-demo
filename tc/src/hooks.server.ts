import PocketBase from 'pocketbase';
import type { Handle } from '@sveltejs/kit';

export const handle: Handle = async ({ event, resolve }) => {
	event.locals.pb = new PocketBase('https://pocketbase-test.tysonjenkins.dev');
	event.locals.pb.authStore.loadFromCookie(event.request.headers.get('cookie') || '');
	const record = event.locals.pb.authStore.record;

	try {
		if (event.locals.pb.authStore.isValid) {
			event.locals.pb.collection('users').authRefresh();
			event.locals.user = structuredClone(record);
		}
	} catch {
		event.locals.pb.authStore.clear();
		event.locals.user = null;
	}

	const response = await resolve(event);
	response.headers.set('set-cookie', event.locals.pb.authStore.exportToCookie({ secure: false }));

	return response;
};
