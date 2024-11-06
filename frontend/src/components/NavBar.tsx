import { Button } from "./ui/button";

import Link from 'next/link';

export default function NavBar() {
  // const handleLoginClick = () => {
  //   window.location.href = '/login';
  // };

  return (
    <div className="z-1 flex justify-between p-5">
      <Link href="/">
        <h1 className="text-2xl font-bold">Podcastify</h1>
      </Link>
      <div className="flex gap-5">
        <Link href="/login">
          <Button>
          Login
          </Button>
        </Link>
        <Link href="/register">
          <Button>
          Register
          </Button>
        </Link>
      </div>
    </div>
  );
} 