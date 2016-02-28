Title: Understanding Config in Elixir
Author: Sheldon Kreger
Category: Programming
Tags: Programming, Elixir
Date: 2016-02-28 12:00

Elixir uses a build tool called Mix, which allows you to define static global variables for your project inside a special file called `config.exs`.

A typical `config.exs` file looks something like this:

    use Mix.Config

    config MyApp,
      myVar: value,
      myVar2: value2

Inside your application, we then load the variables using a function called [`Application.get_env()/3`.](http://elixir-lang.org/docs/stable/elixir/Application.html#get_env/3) This allows us to access the static variables as we desire.

I recently started using Ecto, which uses such configuration to define connection parameters to the database. However, since I already had configuration for some variables inside my application, I was a bit confused about how to properly add the parameters for Ecto. Do I place it all inside the MyApp config? Do I place it inside a new config called `EctoConfig`? Tough to say.

Under the hood, `config` is actually just a key/value list. You may define multiple `configs`, but they are stored as a list of lists, one list for each key you define. For each key, you have another key/value list, which is the actual variables. An example will make this clear.

Let's assume I have an application called StatusApp. I have a file called `repo.ex` which contains a module where I set up my Ecto repository:

    defmodule StatusApp.Repo do
      use Ecto.Repo, otp_app: StatusApp, adapter: Ecto.Adapters.Postgres

      def url do
        "ecto://postgres:postgres@localhost/sn"
      end

    end

I also have a `config.exs` file:

    config StatusApp,
      sites: ["sheldonkreger.com", "prodrumblog.com"],
      interval: 2000

    config StatusApp, StatusApp.Repo,
      adapter: Ecto.Adapters.Postgres,
      database: "sn",
      username: "postgres",
      password: "postgres",
      hostname: "localhost"

    config StatusApp, Foo,
      fooVar: "fooVal"


I like to think of `MyApp` as the top-level identifier for the `config`, and each additional `config` declaration as a separate namespace inside it.

The easiest way to see what this actually looks like is to use [`Application.get_all_env(StatusApp)`:](http://elixir-lang.org/docs/stable/elixir/Application.html#get_all_env/1)

`IO.inspect(Application.get_all_env(StatusApp))` returns:

    [{StatusApp.Repo,
      [adapter: Ecto.Adapters.Postgres, database: "sn", username: "postgres",
       password: "postgres", hostname: "localhost"]}, {Foo, [foo: "fooVal"]},
     {:sites, ["sheldonkreger.com", "prodrumblog.com"]}, {:interval, 2000}]

I can access these variables using the key/value pair as an argument to [`Application.get_env()/3`:](http://elixir-lang.org/docs/stable/elixir/Application.html#get_env/3)

`IO.inspect(Application.get_env(StatusApp, :sites))`

returns:

`["sheldonkreger.com", "prodrumblog.com"]`

We can give it just two arguments because it will default to the top-level list when we don't specify the `key`.

To drill down to `Foo`, we use [`Application.get_env()/3`:](http://elixir-lang.org/docs/stable/elixir/Application.html#get_env/3)

`IO.inspect(Application.get_env(StatusApp, Foo, :fooVar)`

Which returns:

`[fooVar: "fooVal"]`
