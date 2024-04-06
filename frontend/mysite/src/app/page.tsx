import Link from "next/link";

export default function Home() {
  return (
    <>
      <h1 className="text-3xl font-bold underline">pqrst1987's page</h1>
      <div id="contents" className="flex flex-col">
        <Link href={'/games'}>Games</Link>
        <Link href={'/sources'}>Sources</Link>
        <Link href={'/aboutme'}>About me</Link>
        <Link href={'/links'}>Links</Link>
      </div>
    </>
  );
}