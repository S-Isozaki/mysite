import Link from "next/link"

export default function Layout() {
  return (
    <>
    <div id="links" className="flex flex-col">
      <Link href={'https://github.com/S-Isozaki'}>github</Link>
      <Link href={'https://qiita.com/pqrst1987'}>qiita</Link>
      <Link href={'https://onlinejudge.u-aizu.ac.jp/status/users/pqrst'}>data structures</Link>
    </div>
    </>
  )
}