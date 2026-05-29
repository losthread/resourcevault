import Sidebar from "./blocks/Sidebar";
import Post from './blocks/Post';
import Inspect from './blocks/Inspect';

export default function Content() {
  return (
    <main className="flex lg:gap-8">
      <Sidebar />
      <section className='flex flex-col flex-1 lg:mt-10 lg:gap-6'>
        <Post />
        <Post />
      </section>
      <Inspect />
    </main>
  )
}