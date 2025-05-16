<script lang="ts">
  export let form;
</script>

<div class="text-white flex items-center justify-center min-h-screen px-4">
  <div class="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
    <h1 class="text-3xl font-bold text-center mb-6">TYSONCLOUD Signup</h1>
    <form action="?/signup" method="post" class="space-y-4">
      <div>
        <label for="username" class="block text-sm font-medium">Username</label>
        <input
          type="text"
          id="username"
          name="username"
          required
          class="w-full px-4 py-2 bg-gray-700 text-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
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
          class="w-full px-4 py-2 bg-gray-700 text-gray-400 border border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
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
          class="w-full px-4 py-2 bg-gray-700 border text-gray-400  border-gray-600 rounded-md focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
          placeholder="Confirm your password"
        />
      </div>
      {#if form?.error}
        <p class="bg-red-500 p-[8px] rounded-md">{form?.error}</p>
      {/if}
      <button
        type="submit"
        class="w-full py-2 bg-indigo-600 hover:bg-indigo-700 rounded-md font-semibold transition duration-200"
      >
        Sign Up
      </button>
    </form>
    <p class="text-center mt-4 text-sm">
      Already have an account? <a href="/" class="text-indigo-400 hover:underline">Log In</a>
    </p>
    <br>
    <p class="text-center">DO NOT FORGET YOUR PASSWORD BECAUSE THERE IS NO WAY FOR US TO HELP YOU REMEMBER IT</p>
  </div>
</div>
