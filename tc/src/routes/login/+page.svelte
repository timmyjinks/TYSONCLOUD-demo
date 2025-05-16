<script lang="ts">
  import {enhance} from "$app/forms"
  export let form;
</script>
<div class="text-white flex items-center justify-center min-h-screen px-4">
  <div class="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
    <h1 class="text-3xl font-bold text-center mb-6">TYSONCLOUD Login</h1>
    <form action="?/login" use:enhance method="post" class="space-y-4">
      <div>
        <label for="username" class="block text-sm font-medium">Username</label>
        <input
          type="text"
          id="username"
          name="username"
          required
          class="w-full px-4 text-gray-400 py-2 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
          placeholder="Enter your username"
        />
      </div>
      <div>
        <label for="password" class="block text-sm font-medium">Password</label>
        <input
          type="password"
          id="password"
          name="password"
          required
          class="w-full px-4 py-2 text-gray-400 bg-gray-700 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
          placeholder="Enter your password"
        />
      </div>
      {#if form?.error}
        <p class="p-[8px] bg-red-500 rounded-md">{form?.error}</p>
      {/if}
      <button
        type="submit"
        class="w-full py-2 bg-indigo-600 hover:bg-indigo-700 rounded-md font-semibold transition duration-200"
      >
        Log In
      </button>
    </form>
    <p class="text-center mt-4 text-sm">
      Don't have an account? <a href="/signup" class="text-indigo-400 hover:underline">Sign Up</a>
    </p>
  </div>
</div>
