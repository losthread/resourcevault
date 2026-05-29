import { Folder } from "lucide-react"
import {
  Card,
  CardContent,
  CardTitle
} from "../ui/card"


export default function Inspect() {
  return (
    <Card className='h-fit lg:my-7 lg:mr-7 lg:max-w-120 lg:min-w-65 bg-olive-900/50 overflow-y-auto max-h-screen'>
      <CardContent className='border rounded-2xl py-5 mx-5 bg-olive-900/20 overflow-x-scroll'>
        <CardTitle className='mb-5'>
          <p>Recently Visited Folders</p>
        </CardTitle>

        <ul className='flex flex-col lg:gap-3 ml-3 mb-2'>
          <li className='flex lg:gap-2 items-center text-white/90'>
            <Folder className='text-amber-400' />
            Networks
          </li>
          <li className='flex lg:gap-2 items-center text-white/90'>
            <Folder className='text-amber-400' />
            Software Development
          </li>
          <li className='flex lg:gap-2 items-center text-white/90'>
            <Folder className='text-amber-400' />
            Linear Algebra
          </li>
        </ul>
      </CardContent>

      <CardContent className='border rounded-2xl lg:py-5 lg:mx-5 lg:max-w-60 bg-olive-900/20 overflow-x-scroll'>
        <CardTitle className='mb-5'>
          <p>Recommended</p>
        </CardTitle>

        <ul className='flex flex-col lg:gap-3 lg:ml-3 lg:mb-2'>
          <li className='flex lg:gap-2 items-center text-white/90'>
            <Folder className='text-amber-400' />
            Machine Learning
          </li>
          <li className='flex lg:gap-2 items-center text-white/90'>
            <Folder className='text-amber-400' />
            Operating Systems
          </li>
          <li className='flex lg:gap-2 items-center text-white/90'>
            <Folder className='text-amber-400' />
            Geometry
          </li>
        </ul>
      </CardContent>
    </Card>
  )
}