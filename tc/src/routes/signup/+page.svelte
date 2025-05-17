<script lang="ts">
	export let form;
</script>

<div class="flex min-h-screen items-center justify-center px-4 text-white">
	<div class="w-full max-w-lg rounded-lg bg-gray-800 p-8 shadow-lg">
		<h1 class="mb-6 text-center text-3xl font-bold">
			TYSONCLOUD<span
				style="border-radius: 1000px; color: var(--color-indigo-400); border: 2px solid
              var(--color-indigo-400); padding: 0 8px; margin-left:10px">demo</span
			>
			<br />
			Signup
		</h1>
		<form action="?/signup" method="post" class="space-y-4">
			<div>
				<label for="username" class="block text-sm font-medium">Username</label>
				<input
					type="text"
					id="username"
					name="username"
					required
					class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
					placeholder="Enter your name"
				/>
			</div>
			<div>
				<label for="password" class="block text-sm font-medium">Password</label>
				<input
					type="password"
					id="password"
					name="password"
					required
					class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
					placeholder="Enter your password"
				/>
			</div>
			<div>
				<label for="passwordConfirm" class="block text-sm font-medium">Confirm Password</label>
				<input
					type="password"
					id="passwordConfirm"
					name="passwordConfirm"
					required
					class="w-full rounded-md border border-gray-600 bg-gray-700 px-4 py-2 text-gray-400 transition focus:ring-2 focus:ring-indigo-500 focus:outline-none"
					placeholder="Confirm your password"
				/>
			</div>
			{#if form?.error}
				<p class="rounded-md bg-red-500 p-[8px]">{form?.error}</p>
			{/if}
			<button
				type="submit"
				class="w-full rounded-md bg-indigo-600 py-2 font-semibold transition duration-200 hover:bg-indigo-700"
			>
				Sign Up
			</button>
		</form>
		<p class="mt-4 text-center text-sm">
			Already have an account? <a href="/" class="text-indigo-400 hover:underline">Log In</a>
		</p>
		<br />
		<p class="text-center">
			DO NOT FORGET YOUR PASSWORD BECAUSE THERE IS NO WAY FOR US TO HELP YOU REMEMBER IT
		</p>
	</div>
</div>
